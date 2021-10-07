(define (domain Take-away-3)
	(:objects ?v1)
	(:tercondition (= ?v1 0))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?k 1) (<= ?k 3) (>= ?v1 ?k))
		:effect (assign ?v1 (- ?v1 ?k)))
)