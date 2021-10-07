(define (domain Monotonic_Two_piled_nim)
    (:objects ?v1 ?v2)
    (:type normal)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 ?v1)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (>= ?k 1))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= (- ?v2 ?v1) ?k) (>= ?k 1))
        :effect (assign ?v2 (- ?v2 ?k)))
)