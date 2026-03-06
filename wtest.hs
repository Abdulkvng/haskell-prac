-- wtest.hs

import Data.Char (toUpper)

main :: IO ()
main = do
  putStrLn "Fix following map calls by replacing the _n expression an appropriate function."
  print $ map (+1) [1,2,3,4,5] == [2,3,4,5,6]
  print $ map (^2) [1,2,3,4,5] == [1,4,9,16,25]
  print $ map odd [1,2,3,4,5] == [True,False,True,False,True]
  print $ map even [1,2,3,4,5] == [False,True,False,True,False]
  print $ map (map toUpper) ["a","b","c","d"] == ["A","B","C","D"]
  print $ map length ["apple","banana","cherry"] == [5,6,6]
  print $ map (^3) [1,2,3,4,5] == [1,8,27,64,125]
  print $ map length ["Haskell","is","fun"] == [7,2,3]
  print $ map (\x -> x `div` 10) [10,20,30,40,50] == [1,2,3,4,5]
  print $ map (*2) [1,2,3,4,5] == [2,4,6,8,10]