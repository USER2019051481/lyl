(define (domain odd-or-even-nim)
	(:objects ?v1 ?v2)
	(:tercondition (= ?v1 0))
	(:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 1)))
	(:action odd-take-then-even
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 1) (= ?v2 1) (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 0)))
	(:action odd-take-then-odd
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 1) (= ?v2 1) (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 1)))
	(:action even-take-then-even
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 0) (= ?v2 0) (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 0)))
	(:action even-take-then-odd
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 0) (= ?v2 0) (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 1)))
)