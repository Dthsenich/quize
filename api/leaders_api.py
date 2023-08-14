from api import api_bp
from databace import get_top_5_leaders_db


# Url для получения списка лидеров
@api_bp.route('/leaders/<int:level>', methods=['GET'])
def get_top_5(level: int = 0):
    result = get_top_5_leaders_db(level)
    leaders = []

    # проходимся по каждому объекту из списка result

    for leader in result:
        print(leader)
        leaders.append({leader.user_fk.name: leader.score})

    return {'level': level, 'leaders': None}