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
