(define (domain Min-Game)
	(:objects ?v1 ?v2)
	(:tercondition (and (>= ?v1 0)(<= ?v2 2) (>= ?v2 0) (> (+ ?v1 ?v2) 0) (or (= ?v1 0) (= ?v2 0))))
    (:constraint (and (>= ?v1 0) (> (+ ?v1 ?v2) 0) (>= ?v2 0) (<= ?v2 2)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?v2) (<= ?k ?v2) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?v1) (<= ?k ?v1) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
)