(define (domain Subtraction_game)
	(:objects ?v1)
	(:tercondition (and (>= ?v1 0) (< ?v1 3) ))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?v1 ?k) (or (= ?k 3) (= ?k 6) (= ?k 7) (= ?k 8)))
		:effect (assign ?v1 (- ?v1 ?k)))
)