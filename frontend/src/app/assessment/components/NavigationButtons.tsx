"use client";

import { Button } from "@/components/ui/button";

interface Props {
    current: number;
    total: number;
    onNext: () => void;
    onPrevious: () => void;
    disabled?: boolean;
}

export default function NavigationButtons({
    current,
    total,
    onNext,
    onPrevious,
    disabled,
}: Props) {

  return (

    <div className="flex justify-between mt-8">

      <Button
        variant="outline"
        disabled={current === 1}
        onClick={onPrevious}
      >
        Previous
      </Button>

      <Button
    onClick={onNext}
    disabled={disabled}
>
    {current === total ? "Submit" : "Next"}
</Button>

    </div>

  );
}