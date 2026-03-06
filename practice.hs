-- this is a comment

nums = [1,2,3,4,5,6,7,8]

doubleMe :: [Int] -> [Int]
doubleMe = map (*2)


main :: IO ()
main = do
    putStrLn "Hello"
    print $ doubleMe nums

-- Haskell functions

