class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1

    def nextPage(self):
        if self.currentPage < self.numPages():
            self.currentPage += 1

    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = self.numPages()

    def goToPage(self, page):
        if page >= 1 and page <= self.numPages():
            self.currentPage = page

    def numPages(self):
        return (len(self.items) + self.pageSize - 1) // self.pageSize


if __name__ == "__main__":
    alphabetList = "abcdefghijklmnopqrstuvwxyz".split(' ')
    p = Pagination(alphabetList, 4)
    # print(p.getVisibleItems())  # ["a", "b", "c", "d"]
    # p.nextPage()
    # print(p.getVisibleItems())  # ["e", "f", "g", "h"]
    # p.lastPage()
    # print(p.getVisibleItems())  # ["y", "z"]
    # print(len(p.items))
    obj= Pagination()
    print(obj.items)
