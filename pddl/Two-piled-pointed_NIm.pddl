(define (domain Two-piled-pointed_NIm)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (>= ?v1 0) (>= ?v2 0) (> ?v3 0) (<= ?v3 2) (or (= ?v1 0) (= ?v2 0))))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (> ?v3 0) (<= ?v3 2)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (= ?v3 1) (> ?k 0))
        :effect    (and (assign ?v1 (- ?v1 ?k)) (assign ?v3 2)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (= ?v3 2)  (> ?k 0))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v3 1)))
)