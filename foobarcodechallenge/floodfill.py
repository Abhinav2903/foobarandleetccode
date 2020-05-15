class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        rows = len(image)
        cols = len(image[0])
        print(rows)
        print(cols)
        color_to_change = image[sr][sc]
        
        def colorchange(rn, cn):
            nonlocal rows, cols, newColor, image
            
            if rn < 0 or cn < 0 or rn>rows-1 or cn>cols-1 or image[rn][cn]==newColor or image[rn][cn]!=color_to_change:
                return
            
            image[rn][cn] = newColor
            
			# radiate in four directions
            colorchange(rn+1,cn)
            colorchange(rn-1,cn)
            colorchange(rn,cn+1)
            colorchange(rn,cn-1)
        
        colorchange(sr, sc)
        
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
    