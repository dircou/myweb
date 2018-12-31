def test(request):
    import re
    from_data = Article.objects.all()
    print("获取数据库长度:",len(from_data))
    content1 = []
    image = []
    image1 = re.compile('<img.*?src="(.*?)".*?/>', re.S | re.I)
    for i in form_date:
        tem = i.content
        image.append(image1.search(tem).group(1))
        tem = re.sub('<.*?>', '', tem)
        content1.append(re.sub('\s{2,}', '', tem))
