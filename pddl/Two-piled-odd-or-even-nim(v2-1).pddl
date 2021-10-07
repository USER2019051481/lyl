(define (domain odd-or-even-nim)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 0) (= ?v2 0) (>= ?v3 0) (<= ?v3 1)))
	(:constraint (and (>= ?v1 0) (>= ?v2 0)(>= ?v3 0) (<= ?v2 1) (<= ?v3 1)))
	(:action take-then-even1
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 ?v3)  (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v3 0)))
	(:action take-then-odd1
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 ?v3)  (>= ?v1 ?k))
		:effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v3 1)))
	(:action take-then-even2
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 ?v3)  (>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v3 0)))
	(:action take-then-odd2
		:parameters (?k)
		:precondition (and (>= ?k 1) (%= ?k 2 ?v3)  (>= ?v2 ?k))
		:effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v3 1)))
)