class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html3(self,datas):
        fout = open('output.html', 'w', encoding="utf-8")

        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table border = 1>")

        for data in datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['cl'])
            fout.write("<td>%s</td>" % data['xl'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()