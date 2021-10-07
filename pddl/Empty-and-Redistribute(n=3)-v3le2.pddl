(define (domain Empty-and-Redistribute)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 1) (= ?v2 1) (= ?v3 1))
    (:constraint (and (>= ?v1 1) (>= ?v2 1) (>= ?v3 1) (<= ?v3 2)))
    (:action empty1
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> (+ ?v2 ?v3) 2) (= (+ ?v2 ?v3) (+ ?k1 (+ ?k2 ?k3))) (> ?k1 0) (> ?k2 0) (> ?k3 0))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
    (:action empty2
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> (+ ?v1 ?v3) 2) (= (+ ?v1 ?v3) (+ ?k1 (+ ?k2 ?k3))) (> ?k1 0) (> ?k2 0) (> ?k3 0))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
    (:action empty3
        :parameters (?k1 ?k2 ?k3)
        :precondition (and (> (+ ?v1 ?v2) 2) (= (+ ?v1 ?v2) (+ ?k1 (+ ?k2 ?k3))) (> ?k1 0) (> ?k2 0) (> ?k3 0))
        :effect (and (assign ?v1 ?k1) (assign ?v2 ?k2) (assign ?v3 ?k3)))
)