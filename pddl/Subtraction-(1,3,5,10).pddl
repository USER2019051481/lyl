(define (domain Subtraction_game)
	(:objects ?v1)
	(:tercondition (and (>= ?v1 0) (< ?v1 1) ))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?v1 ?k) (or (= ?k 1) (= ?k 3) (= ?k 5) (= ?k 10)))
		:effect (assign ?v1 (- ?v1 ?k)))
)