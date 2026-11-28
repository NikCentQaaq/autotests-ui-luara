from pathlib import Path

import allure
from playwright.sync_api import Playwright, Page
from pytest_playwright.pytest_playwright import browser_type

from config import settings, Browser




def initialize_playwright_page(
        playwright: Playwright,
        browser_type: Browser,
        test_name: str,
        request,
        storage_state: str | None = None
) -> Page:
    """
    Создает и настраивает объект Page Playwright для выполнения теста.

    Выполняет:
    - запуск указанного браузера;
    - создание нового BrowserContext;
    - настройку базового URL, записи видео, trace и storage state;
    - создание новой страницы.

    После завершения теста:
    - сохраняет trace и видео;
    - прикладывает их к Allure только при падении теста;
    - удаляет артефакты успешных тестов;
    - закрывает браузер.
    """

    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    trace_path = settings.tracing_dir.joinpath(f'{test_name}.zip')
    context.tracing.stop(path=trace_path)

    video_path = Path(page.video.path())

    browser.close()

    # Прикладывать артефакты, если тест упал
    rep_call = getattr(request.node, "rep_call", None)

    if rep_call is not None and rep_call.failed:

        allure.attach.file(trace_path, name="trace", extension="zip")
        allure.attach.file(video_path, name="video", attachment_type=allure.attachment_type.WEBM)

    else:
        trace_path.unlink(missing_ok=True)
        video_path.unlink(missing_ok=True)




    # allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)






