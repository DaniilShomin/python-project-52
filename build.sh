#!/usr/bin/env bash
# скачиваем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# здесь добавьте все необходимые команды для установки вашего проекта
# команду установки зависимостей, сборки статики, применения миграций и другие
make install

psql -h dpg-d1cr1emmcj7s73b97lbg-a.oregon-postgres.render.com -U db_task_manager_q2ck_user db_task_manager_q2ck

make migrate