(define (domain Take-away-2)
	(:objects ?v1)
	(:tercondition (= ?v1 0))
	(:constraint (>= ?v1 0))
	(:action take
		:parameters (?k)
		:precondition (and (>= ?k 1) (<= ?k 2) (>= ?v1 ?k))
		:effect (assign ?v1 (- ?v1 ?k)))
)