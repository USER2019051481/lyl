(define (domain Three-piled-pointed_NIm)
	(:objects ?v1 ?v2 ?v3 ?p)
	(:tercondition (and (= ?v1 0) (= ?v2 0) (= ?v3 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0) (<= ?v3 1) (> ?p 0) (<= ?p 3)))
    (:action take1
        :parameters (?k ?m)
        :precondition (and (>= ?v1 ?k) (= ?p 1) (> ?k 0) (> ?m 0) (<= ?m 3))
        :effect    (and (assign ?v1 (- ?v1 ?k)) (assign ?p ?m)))
    (:action take2
        :parameters (?k ?m)
        :precondition (and (>= ?v2 ?k) (= ?p 2)  (> ?k 0) (> ?m 0) (<= ?m 3))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?p ?m)))
    (:action take3
        :parameters (?k ?m)
        :precondition (and (>= ?v3 ?k) (= ?p 3)  (> ?k 0) (> ?m 0) (<= ?m 3))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?p ?m)))
)