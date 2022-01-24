# 添加管理员账户
docker exec -it superset_app superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@superset.com \
               --password admin
# 新增新表
docker exec -it superset_app superset db upgrade
# 加载数据
docker exec -it superset_app superset load_examples
# 初始化数据
docker exec -it superset_app superset init