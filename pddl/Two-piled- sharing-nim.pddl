(define (domain Two-piled-Sharing-nim)
	(:objects ?v1 ?v2)
	(:tercondition (and  (or (= (- ?v2 ?v1) 1)  (=  ?v2 ?v1))  (>= ?v1 0) (>= ?v2 0) (>= ?v2 ?v1)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v2 ?v1)))
    (:action take
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (>= (- ?v2 ?k) (+ ?v1 ?k)))
        :effect (and (assign ?v2 (- ?v2 ?k)) (assign ?v1 (+ ?v1 ?k))))
)