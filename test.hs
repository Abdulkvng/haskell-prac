main :: IO ()
main = do
  putStrLn "Fix following map calls by replacing the _n expression an appropriate function."
  print $ map _1 [1,2,3,4,5] == [2,3,4,5,6]
  print $ map _2 [1,2,3,4,5] == [1,4,9,16,25]
  print $ map _3 [1,2,3,4,5] == [True,False,True,False,True]
  print $ map _4 [1,2,3,4,5] == [False,True,False,True,False]
  print $ map _5 ["a","b","c","d"] == ["A","B","C","D"]
  print $ map _6 ["apple","banana","cherry"] == [5,6,6]
  print $ map _7 [1,2,3,4,5] == [1,8,27,64,125]
  print $ map _8 ["Haskell","is","fun"] == [7,2,3]
  print $ map _9 [10,20,30,40,50] == [1,2,3,4,5]
  print $ map _10 [1,2,3,4,5] == [2,4,6,8,10]