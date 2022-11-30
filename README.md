# Project-1

## BeautifulSoup
- Thường được tích hợp trong package python3, nếu không cài đặt bằng: pip3 install beautifulsoup4

![image](https://user-images.githubusercontent.com/68491164/204843711-bebb30de-b943-407c-bc71-2b6204f97f2b.png)

- Cài đặt framework lxml (tùy chọn): sudo apt-get install python3-lxml

![image](https://user-images.githubusercontent.com/68491164/204843754-4216c811-f6dc-4da1-98cc-7bf6ed322ca8.png)

- Hướng dẫn sử dụng cơ bản:
- Xem xét đoạn code sau:

![image](https://user-images.githubusercontent.com/68491164/204843883-17db818c-360a-4c2b-bfe0-5ba46d88a1de.png)

Import hàm và từ thư viện:

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

![image](https://user-images.githubusercontent.com/68491164/204843930-e83d2bac-cd34-4d8e-813b-12d7a52d0220.png)

- Trích xuất thẻ title (đầu tiên)

```
soup.title
```

![image](https://user-images.githubusercontent.com/68491164/204843976-8bd9a3d9-2560-4322-8fc3-aa85915aa1b2.png)

- Tên thẻ title

```
soup.title.name
```

![image](https://user-images.githubusercontent.com/68491164/204844003-3e4de3d8-8ee4-46ba-88ba-17130c90cc38.png)

- Giá trị chuỗi thẻ title

```
soup.title.string
```

![image](https://user-images.githubusercontent.com/68491164/204844050-1a291ddc-829f-4b7b-b11c-3d527ffbbd57.png)

- Tên thẻ cha của title

```
soup.title.parent.name
```

![image](https://user-images.githubusercontent.com/68491164/204844085-89a0d1e8-8f20-4526-bdc5-6454b7fa3d99.png)

- Thẻ p (đầu tiên)

```
soup.p
```

![image](https://user-images.githubusercontent.com/68491164/204844111-62caf5a2-d6e3-4622-8afc-ba81b6f52355.png)

- Giá trị thuộc tính class trong thẻ p

```
soup.p['class']
```

![image](https://user-images.githubusercontent.com/68491164/204844134-7bb1f973-609a-4d0e-9a24-d33c9ef75b8c.png)

- Thẻ a (đầu tiên)

```
soup.a
```

![image](https://user-images.githubusercontent.com/68491164/204844170-6a05fdff-ec69-445c-b83f-6435a1e4eed9.png)

- Tất cả thẻ a

```
soup.find_all('a')
```

![image](https://user-images.githubusercontent.com/68491164/204844215-ab534545-079a-43b4-b82c-2557c484f5c5.png)

- Tìm kiếm thẻ có id="link3"

```
soup.find(id="link3")
```

![image](https://user-images.githubusercontent.com/68491164/204844264-8c7b6a99-0d07-4992-b71c-e4c3ae2fbf58.png)

- In ra lần lượt từng thẻ a

```
for link in soup.find_all('a'):
    print(link.get('href'))
```

![image](https://user-images.githubusercontent.com/68491164/204844293-bfb33615-136d-4512-9435-dd1905d769dc.png)

- In ra tất cả text

```
print(soup.get_text())
```

![image](https://user-images.githubusercontent.com/68491164/204844313-d68eb434-7522-4724-b601-9f3bf15defce.png)

## Tham khảo
- https://beautiful-soup-4.readthedocs.io/en/latest/

