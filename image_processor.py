import cv2
from bs4 import BeautifulSoup
from qreader import QReader

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_html_content(link):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(link)
        driver.implicitly_wait(10)  # Wait for JS to load
        content = driver.page_source
        return content
    finally:
        driver.quit()

'''
def get_html_content(link):
    result_queue = queue.Queue()
    
    def run_playwright():
        async def scrape():
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=True,
                    args=[
                        '--no-sandbox',
                        '--disable-dev-shm-usage',
                        '--disable-gpu',
                        '--disable-web-security'
                    ]
                )
                page = await browser.new_page()
                await page.goto(link, wait_until='networkidle')
                content = await page.content()
                await browser.close()
                return content
        
        # Create new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(scrape())
            result_queue.put(('success', result))
        except Exception as e:
            result_queue.put(('error', str(e)))
        finally:
            loop.close()
    
    # Run in separate thread
    thread = threading.Thread(target=run_playwright)
    thread.start()
    thread.join(timeout=30)  # 30 second timeout
    
    if thread.is_alive():
        raise Exception("Playwright operation timed out")
    
    result_type, result_data = result_queue.get()
    if result_type == 'error':
        raise Exception(f"Playwright error: {result_data}")
    
    return result_data

def get_html_content(url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        rendered_html = page.content()

        browser.close()
    
    return (rendered_html)'''

def get_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()


def load_image(file_name):
    img = cv2.imread(file_name)
    return img

def detect_qr_code(img):
    qreader = QReader()

    data = qreader.detect_and_decode(image=img)
    
    if data[0]:
        return data[0]
    else:
        return None