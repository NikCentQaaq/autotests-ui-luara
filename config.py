from enum import StrEnum
from typing import Self

from pydantic import HttpUrl, DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(StrEnum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"




class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        extra='allow',

        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: HttpUrl
    headless: bool
    browser: list[Browser]

    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath


    @classmethod
    def setup(cls) -> Self:
        """
        Создает необходимые директории и файлы проекта,
        затем возвращает инициализированный экземпляр Settings.
        """

        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")
        browser_state_file = FilePath("browser-state.json")

        # Создание директорий, если они не существуют
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.setup()







