(* Problem 5 *)
(* Returns a list of tuples consisting of x and F(x)
where F(x) is a function being applied to x
and x is = a, a+d, a+ 2d, ..., a +nd *)

(* Creates a list of x values *)
fun tabulateHelper(a:real, d:real, n: int, count) = if count =0 then [a]@tabulateHelper(a, d, n, 1) 
                                                    else  if count =n then [a+(d*Real.fromInt(n))]
                                                    else [a+(d*Real.fromInt(count))]@tabulateHelper(a,d,n,count+1);

(* combines two lists, in this case the x list and the F(x) list *)
fun combineTwoLists([], []) = []
    | combineTwoLists(hd::tl, []) = []
    | combineTwoLists([], hd2::tl2) = []
    | combineTwoLists(hd1::tl1, hd2::tl2) = [[hd1]@[hd2]]@combineTwoLists(tl1, tl2);

(* Test functions *)
fun square(x: real) = x*x;
fun thirdPower(x: real) = x*x*x;

(* maps a list to a function *)
fun mappingFunction([]:real list, F) = nil
    | mappingFunction(hd::tl, F) = F(hd)::mappingFunction(tl, F);


fun tabulate(a: real, d: real, n: int, F) = combineTwoLists(tabulateHelper(a,d,n,0), mappingFunction(tabulateHelper(a,d,n,0),F));

(* Testing with two different Inputs *)
val test1 = tabulate(0.1, 2.0, 2, square);
val test2 = tabulate(1.0, 2.0, 3, thirdPower);
(* Output:
val test1 = [[0.1,0.01],[2.1,4.41],[4.1,16.81]] : real list list
val test2 = [[1.0,1.0],[3.0,27.0],[5.0,125.0],[7.0,343.0]] : real list list *)


(* use "/Users/sabrinamargetic/Documents/SPRING 2020/CSE 307/Homework_2/Problem_5.sml"; *)





