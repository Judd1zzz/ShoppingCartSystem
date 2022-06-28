from environs import Env
from dataclasses import dataclass


@dataclass
class DbConfig:
    path: str


@dataclass
class TgBot:
    token: str
    payments_token: str
    admin_ids: list[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            payments_token=env.str("PAYMENTS_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
        ),
        db=DbConfig(
            path='data/botBD.sqlite',
        ),
        misc=Miscellaneous()
    )
