(define (domain staircase)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 0)(= ?v2 0) (= ?v3 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 (+ ?v1 ?k))))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0))
        :effect (and (assign ?v3 (- ?v3 ?k)) (assign ?v2 (+ ?v2 ?k))))
)