(define (domain Empty_and_divide)
    (:objects ?v1 ?v2)
    (:type normal)
    (:tercondition (and (= ?v1 1) (= ?v2 1)))
    (:constraint (and (>= ?v1 1) (>= ?v2 1)))
    (:action empty1
        :parameters (?k)
        :precondition (and (> ?v2 ?k) (>= ?k 1))
        :effect (and (assign ?v1 ?k) (assign ?v2 (- ?v2 ?k))))
    (:action empty2
        :parameters (?k)
        :precondition (and (> ?v1 ?k) (>= ?k 1))
        :effect (and (assign ?v2 ?k) (assign ?v1 (- ?v1 ?k))))
)