import os
import shutil
import sys
from datetime import datetime

import pytest
from huskypo import logconfig

from framework import cleaning, allure_generator
from framework import path, common

if __name__ == "__main__":

    logconfig.basic(path.Log.LOG)

    TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_dir= os.path.join(path.REPORTS,TIMESTAMP)
    report_path= os.path.join(report_dir,f"allure_{TIMESTAMP}.html")
    common.write_txt_by(path.Base.TIMESTAMP_TXT, TIMESTAMP)

    # pytest.main()
    # pytest.main(['--platform','ios',"-m","iWA_login","--app_path",'/Users/twinb00551192/Desktop/QA_file/iWA-DEV.app'])
    # pytest.main([
    #     '--platform','android',
    #     '-m','android_login',
    #     '--app_path','/Users/twinb00551192/Desktop/ihv-app-android-UAT/app-artifact.apk',
    #     '--alluredir=./reports/allure_tmp'
    # ])
    pytest.main([
        '--platform','ios',
        '-m','iWA_login',
        '--app_path','/Users/twinb00551192/Desktop/QA_file/iWA-DEV.app',
        # '--app_path','/Users/twinb00551192/Desktop/WMSAPP-QA-IOS/iWA-DEV.app'
        '--alluredir','./reports/allure_tmp',
        '-n','2'
    ])


    allure_generator.output_allure_html()
    # 複製html到根目錄
    shutil.copyfile(f"{report_path}",f"{path.BASE}/output.html")
    # 刪除report dir
    shutil.rmtree(report_dir)

    cleaning.remove_logs()
    cleaning.remove_allure_tmp()