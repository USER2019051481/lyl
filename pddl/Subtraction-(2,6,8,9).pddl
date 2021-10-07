(define (domain Subtraction_game)
	(:objects ?v1)
	(:tercondition (and (>= ?v1 0) (< ?v1 2) ))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?v1 ?k) (or (= ?k 2) (= ?k 6) (= ?k 8) (= ?k 9)))
		:effect (assign ?v1 (- ?v1 ?k)))
)