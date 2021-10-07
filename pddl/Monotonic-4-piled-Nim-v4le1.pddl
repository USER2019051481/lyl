(define (domain Two-piled-nim)
	(:objects ?v1 ?v2 ?v3 ?v4 )
	(:tercondition (and (= ?v1 0) (= ?v2 0) (= ?v3 0) (= ?v4 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (>= ?v2 ?v1) (>= ?v3 ?v2) (>= ?v4 ?v3)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= (- ?v2 ?k) ?v1) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= (- ?v3 ?k) ?v2) (> ?k 0))
        :effect (assign ?v3 (- ?v3 ?k)))
    (:action take4
        :parameters (?k)
        :precondition (and (>= (- ?v4 ?k) ?v3) (> ?k 0))
        :effect (assign ?v4 (- ?v4 ?k)))
)