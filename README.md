## Architectural decisions

This project consists of two services `bot` and `database`.

Service `bot` is developed based on aiogram rpc.

### Bot Commands and Actions

#### /start

Runs chat with bot. 

Bot's output:

```telegram

Hi! I'm avare in video statistics. Write me and I'll help you.
```

Next you can write your requests to the bot what data you would like to receive in 
natural language.

#### User inputs

```Write your desirable request```

Bot's output:

```telegram
**Scalar value**
```

### How bot works

Bot processes your request throught using `MistralAi` LLM rpc[https://docs.mistral.ai/api/endpoint/chat#operation-chat_completion_v1_chat_completions_post]. 
The used model is `codestral-latest`. The appropriate handler takes user request and send it to the 
`MistralAi` chat. The `MistralApi` rpc send the response with an sql query which is extracted by the 
handler and passed to the database. Next, the sql is executed and the scalar value is send as a result
to the user in the bot chat.

#### Prompt to the MistralAi looks as:

```
сгенерируйте Sql запрос: {user request typed in telegram bot chat}.
    
Описания моделей следующие:

class Video:

    __tablename__ = "video"

    id
    creator_id
    video_created_at
    views_count
    likes_count 
    comments_count
    reports_count 
    created_at
    updated_at


class SnapShot:

    __tablename__ = "snapshot"

    id
    video_id
    delta_views_count
    delta_likes_count
    delta_comments_count
    delta_reports_count
    created_at
    updated_at
```

------------------
------------------

## How to run bot

See the `Commands` section below. Before using the bot, you need to load the json data via `Load json data` 
command. Loading this json [videos.json] will take about 30 minutes. However, you should have the running 
application deployed in docker containers. So, depending on whether the application was built or not,
you should run the appropriate command either `Build and run` or `Run only`.

## Customize settings:

Optionally if you want to set your own MistralAi Api Key you can open the `.env` file and change
`MISTRAL_API_KEY` value to your own key.


## Commands:

### Load json data:

```bash
docker exec -it bot python -m cmds.normalize_json ../videos.json
```

### Build and run:

```bash
docker compose up -d --build
```

### Run only:

```bash
docker compose up -d

```