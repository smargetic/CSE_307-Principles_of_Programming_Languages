(* Problem 4 *)
(* Use mutual recursion in order to get four seperate lists, of every fourth element, starting at 1,2,3, and 4 *)


(* Mutually recursive function that starts at the first index, and takes every fourth from the goal (including the goal) *)
fun takeEveryFourth([], count, goal,mult) =nil
    | takeEveryFourth(hd::tl, count, goal,mult) =
        if count = (goal+(mult*3)) then hd::skip(tl, count, goal,mult+1)
        else skip(tl, count+1, goal, mult)
and skip([], count, goal, mult) = nil
    | skip(hd::tl, count, goal,mult) =
        if count = (goal+(mult*3)) then hd::takeEveryFourth(tl, count, goal, mult+1)
        else takeEveryFourth(tl, count+1,goal, mult);


(* Function to be called upon to create four seperate lists
Creates a big list of the four seperate lists (combines them into one list of lists) *)
fun bigList([], x, [[]]) = []
    | bigList(hd::tl, x, [[]]) = bigList(hd::tl, x+1, [takeEveryFourth(hd::tl, 0,x,0)])
    | bigList(hd::tl, x, hdB::tlB)= if x =4 then hdB::tlB
                        else bigList(hd::tl, x+1, hdB::tlB@[takeEveryFourth(hd::tl, 0,x,0)]);



(* Testing with two different Inputs *)
val test1 = bigList([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0], 0, [[]]);
val test2 = bigList([1,2,3,4,5,6], 0, [[]]);
(* Output:
val test1 = [[1.0,5.0,9.0],[2.0,6.0,10.0],[3.0,7.0],[4.0,8.0]]
  : real list list
val test2 = [[1,5],[2,6],[3],[4]] : int list list*)


(* use "/Users/sabrinamargetic/Documents/SPRING 2020/CSE 307/Homework_2/Problem_4.sml"; *)


