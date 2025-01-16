from agency_swarm.tools import BaseTool
from pydantic import Field
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BrowserWindowAnalyzer(BaseTool):
    """
    A tool to capture and analyze the current browser window's properties, such as dimensions,
    viewport size, and any relevant metadata. It provides insights into the design constraints
    and opportunities based on the browser's capabilities.
    """

    url: str = Field(
        ..., description="The URL of the webpage to analyze."
    )

    def run(self):
        """
        Captures and analyzes the current browser window's properties and returns the information
        in a structured format for further analysis.
        """
        # Set up the Chrome WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            # Open the specified URL
            driver.get(self.url)

            # Capture browser window properties
            window_size = driver.get_window_size()
            viewport_size = driver.execute_script("return {width: window.innerWidth, height: window.innerHeight};")
            page_title = driver.title
            page_url = driver.current_url

            # Prepare the analysis result
            analysis_result = {
                "window_size": window_size,
                "viewport_size": viewport_size,
                "page_title": page_title,
                "page_url": page_url,
                "design_constraints": {
                    "max_width": viewport_size['width'],
                    "max_height": viewport_size['height']
                },
                "opportunities": "Consider responsive design techniques to optimize for various viewport sizes."
            }

            return analysis_result

        finally:
            # Close the WebDriver
            driver.quit()