# Финальный тестовый проект SkillFactory для курса QAP
_________________________________________________________________________________________________________________________________________________________________________
Проект разработан для автоматизированного тестирования UI сайта интернет магазина "Ozon": https://www.ozon.ru/ с использованием PyTest и Selenium.
•	В файле "config" прописаны тестовые данные для выполнения тестов, также информация о базовом URL.
•	В файле "conftest.py" содержится фикстура для используемого вебдрайвера Chrome. В указанном месте необходимо указать путь к вебдрайверу, установленному на вашем компьютере.
•	В файле "test_Main_Page.py" содержатся все используемые в проекте тесты.
•	Папка "pages" содержит: "Base_page" , где находится базовый класс "BasePage", в котором прописаны методы используемые для выполнения тестов. А также "Main_page", где расположены все локаторы, для выполнения тестов.
•	Файл requirements.txt содержит перечень необходимых библиотек для работы проекта.
Представленные в проекте тесты проверяют видимость кнопок на главной странице сайта, корректность их названия, соответствие разделов, куда ведет переход при клике по кнопке.
Запуск тестов осуществляется через кнопку RUN, находясь в "test_Main_Page.py"
Данный проект был написан и протестирован на окружении Windows 10 PRO, Google Chrome: Версия 104.0.5112.102 (Официальная сборка), (64 бит).
