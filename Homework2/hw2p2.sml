(* Problem 2 *)


(* Part A *)
(* Put's the head of the list at the tail *)
fun revCycle([]) = []
    | revCycle(hd::tl) = tl@[hd];

(* Testing part A with two different Inputs *)
val partA_test1 = revCycle([1,2,3,4]);
val partA_test2 = revCycle([1.0, 2.0, 3.0, 4.0, 5.0]);
(* Output:
val partA_test1 = [2,3,4,1] : int list
val partA_test2 = [2.0,3.0,4.0,5.0,1.0] : real list *)


(* Part B *)
(* Puts the head of the list at the tail for a certain number of repitions, i *)
fun revCycles([], i:int) = []
    |revCycles(hd::tl, 0:int) = hd::tl
    | revCycles(hd::tl, i:int) = revCycles(tl@[hd], i-1);

(* Testing part B with two different Inputs *)
val partB_test1 = revCycles([1.0, 2.0, 3.0, 4.0], 2);
val partB_test2 = revCycles(["1.0", "2.0", "3.0", "4.0"], 3);
(* Output:
val partB_test1 = [3.0,4.0,1.0,2.0] : real list
val partB_test2 = ["4.0","1.0","2.0","3.0"] : string list *)



(* use "/Users/sabrinamargetic/Documents/SPRING 2020/CSE 307/Homework_2/Problem_2.sml"; *)
