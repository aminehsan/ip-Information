import traceback
import time
import requests


class IP:
    """A class to retrieve IP information."""

    __BASE_URL = 'http://ip-api.com/json'
    __PARAMS = {'fields': 'status,country,regionName,isp,mobile,proxy,hosting,query'}

    def information(self, proxies: dict = None) -> dict:
        """Fetch IP information."""
        counter = 0
        while True:
            counter += 1
            try:
                r = requests.get(url=self.__BASE_URL, params=self.__PARAMS, proxies=proxies)
                assert (
                        r.status_code == 200 and
                        'application/json' in r.headers['Content-Type'] and
                        r.json()['status'] == 'success'
                ), 'Invalid response or failed status.'
                return r.json()
            except Exception as e:
                print(f'Fetch IP information failed. Counter: {counter}')
                traceback.print_exc()
                if counter >= 5:
                    raise e
                time.sleep(10)


ip = IP()
