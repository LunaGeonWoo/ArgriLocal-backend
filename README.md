환경 설정 커맨드 <br>
`pip install -r requirements.txt`

# API reference

## Users

### `[POST] /users/` [✔]

> Request

| Data     | Description |
| -------- | ----------- |
| username | str         |
| password | str         |
| name     | str         |
| email    | str         |
| address  | str         |

> Response

| Data     | Description |
| -------- | ----------- |
| name     | str: token  |
| username | str: token  |
| address  | str: token  |
| email    | str: token  |
