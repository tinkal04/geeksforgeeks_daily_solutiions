class Solution:
    def largestSubsquare(self, n, a):
        left = [[0] * n for _ in range(n)]
        top = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    if j != 0:
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 1

                    if i != 0:
                        top[i][j] = top[i - 1][j] + 1
                    else:
                        top[i][j] = 1

                    minX = min(top[i][j], left[i][j])
                    while minX > 0:
                        k = i - minX + 1
                        l = j - minX + 1
                        if left[k][j] >= minX and top[i][l] >= minX:
                            ans = max(ans, minX)
                            break
                        minX -= 1

        return ans
