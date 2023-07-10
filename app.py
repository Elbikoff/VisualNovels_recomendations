from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Загрузка данных
data = pd.read_csv('vndb_votes_short.csv', delimiter=' ')  # Замените путь к файлу и укажите пробел в качестве разделителя

# Создание разреженной матрицы взаимодействий пользователей с визуальными новеллами
sparse_ratings = data.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
user_ids = sparse_ratings.index
item_ids = sparse_ratings.columns

# Рассчитать сходство между объектами (визуальными новеллами)
item_similarities = cosine_similarity(sparse_ratings.T)


# Функция для получения рекомендаций
def get_recommendations(user_id):
    try:
        # Получить оценки пользователя
        user_ratings = sparse_ratings.loc[user_id]

        # Проверить, есть ли у пользователя оценки
        if user_ratings.sum() == 0:
            raise TypeError("Пользователь не имеет оценок.")

        # Вычислить веса рекомендаций на основе сходства с оцененными визуальными новеллами
        weighted_ratings = user_ratings.to_numpy().reshape(1, -1) * item_similarities

        # Суммировать взвешенные рейтинги по визуальным новеллам
        weighted_sum = weighted_ratings.sum(axis=1)

        # Отсортировать визуальные новеллы по убыванию взвешенных рейтингов
        recommendations = pd.Series(weighted_sum, index=item_ids).sort_values(ascending=False)

        # Создать DataFrame с идентификаторами новелл и взвешенными рейтингами
        recommendations_df = pd.DataFrame({'item_id': recommendations.index, 'Взвешенный рейтинг': recommendations.values})

        return recommendations_df
    except KeyError:
        return None
    except TypeError:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    profile_link = request.form['profile_link']
    user_id = int(profile_link.split('u')[-1])
    recommendations = get_recommendations(user_id)
    if recommendations is None:
        return render_template('error.html', error_message="Профиль не найден или нет оценок пользователя.")
    else:
        return render_template('recommendations.html', recommendations=recommendations)


@app.route('/resources')
def resources():
    links = [
        {'title': 'VK', 'url': 'https://vk.com/o.elbikov'},
        {'title': 'Telegram', 'url': 'https://t.me/elbikov'},
    ]
    return render_template('resources.html', links=links)

#@app.route('/')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
