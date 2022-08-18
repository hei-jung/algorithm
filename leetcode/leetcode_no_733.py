class Solution(object):

    def floodFill(self, image, sr, sc, color):
        scolor = image[sr][sc]  # starting pixel color

        # 시작점의 색깔이 이미 주어진 색깔이랑 같으면 종료
        if color == scolor: return image

        m, n = len(image), len(image[0])

        def fill(i, j):
            # 이미 채워진 상태면 종료
            if image[i][j] == color: return
            if image[i][j] == scolor:
                image[i][j] = color
                if i - 1 >= 0: fill(i - 1, j)  # 상
                if i + 1 < m: fill(i + 1, j)  # 하
                if j - 1 >= 0: fill(i, j - 1)  # 좌
                if j + 1 < n: fill(i, j + 1)  # 우

        fill(sr, sc)
        return image
