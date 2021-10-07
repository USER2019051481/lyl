(define (domain welter)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= 3 (+ ?v1 (+ ?v2 ?v3))) (>= ?v1 0) (>= ?v2 0) (= ?v3 0) (!= ?v1 ?v2) (!= ?v2 ?v3) (!= ?v1 ?v3))  )
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (= ?v3 0) (!= ?v1 ?v2) (!= ?v2 ?v3) (!= ?v1 ?v3)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (!= (- ?v1 ?k) ?v2) (!= (- ?v1 ?k) ?v3))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0) (!= (- ?v2 ?k) ?v1) (!= (- ?v2 ?k) ?v3))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k)
        :precondition (and (>= ?v3 ?k) (> ?k 0) (!= (- ?v3 ?k) ?v1) (!= (- ?v3 ?k) ?v2))
        :effect (assign ?v3 (- ?v3 ?k)))
)