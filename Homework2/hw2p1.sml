(* Problem 1 *)

(* Part A *)
(* Creates array of 1.0's *)
fun genPoly(n) = if n=0 then []
                else 1.0::genPoly(n-1);


(* Testing part A with two different Inputs *)
val partA_test1 = genPoly(0);
val partA_test2 = genPoly(3);
(* Output:
val partA_test1 = [] : real list
val partB_test2 = [1.0,1.0,1.0] : real list *)

(* Part B *)
(* Evaluates a polynomial with the function evalPoly(L, a) *)

(* length of an array *)
fun length([]) = 0
   |length(hd::tl) = 1 + length(tl);

(* Power function *)
fun power(base, exponent) = if exponent = 0 then 1.0
                            else base*power(base, exponent-1);


(* Helper function to keep track of exponent value *)
fun evalPolyHelper([], a, exponent) = 0.0
    | evalPolyHelper(hd::tl, a, exponent) = hd*power(a, exponent) + evalPolyHelper(tl, a, exponent+1);


 (* Takes in a list representing a polynomial, and a real value, a
 Evaluates the polynomial. *)
fun evalPoly([], a) = 0.0
            | evalPoly(hd::tl, a) = evalPolyHelper(hd::tl,a,0);

(* Testing part B with two different Inputs *)
val partB_test1 = evalPoly([10.0, 3.0, 1.0], 2.0);
val partB_test2 = evalPoly([4.0, 2.0], 3.0);
(* Output:
val partB_test1 = 20.0 : real
val partB_test2 = 10.0 : real *)


(* Part C *)

(* Provides a padding of zero's, number of which depend on the number provided, to a list given *)
fun paddingFunction([] : real list, number: int) = if number =0 then []
                                else paddingFunction([0.0], number-1) 
    | paddingFunction(hd::tl: real list, number: int)= if number = 0 then hd::tl
                                else paddingFunction(0.0::(hd::tl), number-1);


(* Combines two lists *)
fun addLists([]: real list, []: real list) = []
    | addLists(hd::tl: real list, []: real list) = hd::tl
    | addLists([]: real list, hd2::tl2: real list) = hd2::tl2
    | addLists(hd::tl: real list, hd2::tl2: real list) = (hd+hd2)::(addLists(tl, tl2));


(* Multiplies the current head of the first list with all the elements of the second list *)
fun multiplyListAndHead(hd: real, []: real list) = nil
    | multiplyListAndHead(hd:real, hd2::tl: real list) = (hd*hd2)::multiplyListAndHead(hd, tl);


(* Creates the desired list of polynomials
Used as opposed to multPoly because it has a count for padding purposes *)
fun multiplyPolyHelperHelper([], [], count) = nil
    | multiplyPolyHelperHelper([]:real list, hd2::tl2: real list, count) = []
    | multiplyPolyHelperHelper(hd::tl: real list, []: real list, count) = nil
    | multiplyPolyHelperHelper(hd::tl:real list, hd2::tl2: real list, count) = addLists(paddingFunction(multiplyListAndHead(hd, hd2::tl2), count), multiplyPolyHelperHelper(tl, hd2::tl2, count+1));


fun multPoly([]: real list, []: real list) = []
    | multPoly(hd::tl: real list, []: real list)= hd::tl
    | multPoly([]: real list, hd2::tl2: real list) = hd2::tl2
    | multPoly(hd::tl:real list, hd2::tl2: real list) = multiplyPolyHelperHelper(hd::tl, hd2::tl2, 0);
    
(* Testing part C with two different Inputs *)
val partC_test1 = multPoly([~1.0, 1.0], [1.0,1.0]);
val partC_test2 = multPoly([3.0, 1.0,1.0], [2.0,1.0]);
(* Output:
val partC_test1 = [~1.0,0.0,1.0] : real list
val partC_test2 = [6.0,5.0,3.0,1.0] : real list *)




(* use "/Users/sabrinamargetic/Documents/SPRING 2020/CSE 307/Homework_2/Problem_1.sml"; *)
