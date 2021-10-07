(define (domain CircularNIm)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 0) (= ?v2 0) (= ?v3 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0)))
    (:action take1
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (>= ?v1 ?k1) (>= ?v2 ?k2) (>= ?v3 ?k3) (>= ?k1 0) (>= ?k2 0) (>= ?k3 0) (>= (+ ?k1 (+ ?k2 ?k3)) 1))
        :effect (and (assign ?v1 (- ?v1 ?k1)) (assign ?v2 (- ?v2 ?k2)) (assign ?v3 (- ?v3 ?k3))))
)