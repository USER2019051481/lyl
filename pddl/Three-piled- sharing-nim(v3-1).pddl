(define (domain Two-piled-Sharing-nim)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and  (or (= (- ?v2 ?v1) 1)  (=  ?v2 ?v1))  (or (= (- ?v3 ?v2) 1)  (=  ?v3 ?v2))  (>= ?v1 0) (>= ?v2 0) (>= ?v3 0)  (>= ?v3 ?v2) (>= ?v2 ?v1)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v3 0) (<= ?v3 1) (>= ?v3 ?v2)  (>= ?v2 ?v1)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (>= (- ?v2 ?k) (+ ?v1 ?k)))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 (+ ?v1 ?k))))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0) (>= (- ?v3 ?k) (+ ?v2 ?k)))
        :effect (and (assign ?v3 (- ?v3 ?k)) (assign ?v2 (+ ?v2 ?k))))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0) (>= (- ?v3 ?k) (+ ?v1 ?k)))
        :effect (and (assign ?v3 (- ?v3 ?k)) (assign ?v1 (+ ?v1 ?k))))
)