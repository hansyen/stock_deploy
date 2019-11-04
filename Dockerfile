FROM ubuntu
FROM python:3

# Maintainer info
LABEL MAINTAINER Hans Yen <Hans@smartfun.com.tw>

# 透過 apt-get 更新
RUN apt-get update -y
# 透過 apt-get 安裝 python3-pip, python3-dev, build-essential
RUN apt-get install -y python3-pip python3-dev build-essential

# 複製當前目錄裡的檔案到stock-app(container)中
ADD . /stock-app
# 切換工作目錄到stock-app
WORKDIR /stock-app
# pip install
RUN pip install -r requirements.txt

EXPOSE 80

# 執行python指令
ENTRYPOINT ["python"]
# 執行start_api_test.py
CMD ["start_stock.py"]

# FROM nginx
