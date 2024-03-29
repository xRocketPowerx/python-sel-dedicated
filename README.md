
# WIP: Python client for Selectel Servers API

[![Build Status](https://travis-ci.org/kubernetes-client/python.svg?branch=master)](https://travis-ci.com/xRocketPowerx/python-sel-dedicated)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Language: Python](https://img.shields.io/badge/Language-Python%203.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue)

|         |   |
|---------|---|
| status  | WIP |
| version | 0.0.1-beta |


## Назначение
Предоставить python-native интерфейс для работы с Selectel Servers API.


### Цели которые преследует проект

1. Оставаться в контексте любимого языка при работе с API.
    1. Использование функционал и типов языка при работе с API.
    1. Валидация запросов к API на уровне клиентского кода (до запросов в API).
1. Открытость для исправлений и улучшений.
1. Пример проекта с использованием openapi code-generation.


## Пример использования

### Список локаций проекта 

```python

from sel_dedicated.configuration import Configuration
from sel_dedicated.api_client import ApiClient

import sel_dedicated_codegen as dedic

def get_config():
    cfg = Configuration()
    cfg.api_key['X-Token'] = "{paste your access token here}"
    return cfg 


def get_client():
    cfg = get_config()
    client = ApiClient(cfg) 
    return client


def get_locations_api(client):
    return dedic.LocationsApi(client)

def main():
    client = get_client()
    locations_api = get_locations_api(client)
    for loc in locations_api.get_location_view().result:
        print("%s %3s %20s" % (loc.uuid, loc.location_id, loc.name))    


if __name__=="__main__":
    main()

```

### Список услуг серверов 

```python

from sel_dedicated.configuration import Configuration
from sel_dedicated.api_client import ApiClient

import sel_dedicated_codegen as dedic

def get_config():
    cfg = Configuration()
    cfg.api_key['X-Token'] = "{paste your access token here}"
    return cfg 


def get_client():
    cfg = get_config()
    client = ApiClient(cfg) 
    return client


def get_services_api(client):
    return dedic.ServicesApi(client)


def main():
    client = get_client()
    services_api = get_services_api(client)
    for svc in services_api.get_server_list().result:
        print("%s %12s %10s %s" % (svc.uuid, svc.name, svc.state, svc.model))


if __name__=="__main__":
    main()

```

## TODO

1. [x] MVP python client
1. [x] MVP python client auto-generation tooling
1. [x] Интеграция с CI 
1. [ ] Стабилизировать BETA 
1. [ ] Забагрепортить ошибки в swagger документации API
1. [ ] Расширить покрытие тестами.
1. [ ] Стабилизировать API (v1.0.0) и опубликовать в PyPI
1. [ ] Расширить функционал: 
    1. [ ] сгруппировать нэймспейсы API в общий входной объект.


## Authors
Команда RocketPower (Selectel Hackathon 2019)

## License
MIT
