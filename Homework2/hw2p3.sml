(* Problem 3 *)

(* Part A *)
(* Removes first instance of an element in a list *)

(* I check the head of each recursive call
If the head is not a match, I add it to a seperate temp list
If it is, I return the temp list concatenated with the remaining tail of the first list *)
fun removeFstHelper(x, [], []) = []
    | removeFstHelper(x, hd::tl, []) = hd::tl
    | removeFstHelper(x, [], hd2::tl2) = if x =hd2 then tl2
                                            else removeFstHelper(x, [hd2], tl2)
    | removeFstHelper(x, hd1::tl1, hd2::tl2) = if x= hd2 then [hd1]@tl1@tl2
                                                else removeFstHelper(x, [hd1]@tl1@[hd2], tl2);

fun removeFst(x,[])= []
    | removeFst(x, hd::tl) = removeFstHelper(x, [], hd::tl);


(* Testing part A with two different Inputs *)
val partA_test1 = removeFst("3.0",["1.0", "2.0", "3.0", "4.0", "3.0"]);
val partA_test2 = removeFst(3, [1,3,5,4,6,9,4,3,2]); 
(* Output:
val partA_test1 = ["1.0","2.0","4.0","3.0"] : string list
val partA_test2 = [1,5,4,6,9,4,3,2] : int list *)


(* Part B *)
(* Removes the last instance of an element in a list *)

(* I reverse the list, and use the remove first function
I then reverse the list back again *)
fun removeLst(x,[]) = []
    | removeLst(x, hd::tl) = rev(removeFst(x,rev(hd::tl)));


(* Testing part B with two different Inputs *)
val partB_test1 = removeLst(3,[1,3,5,4,6,9,4,3,2]);
val partB_test2 = removeLst("3.0",["1.0", "3.0", "4.0", "3.0", "2.0", "3.0", "4.0"]); 
(* Output:
val partB_test1 = [1,3,5,4,6,9,4,2] : int list
val partB_test2 = ["1.0","3.0","4.0","3.0","2.0","4.0"] : string list *)



(* use "/Users/sabrinamargetic/Documents/SPRING 2020/CSE 307/Homework_2/Problem_3.sml"; *)
