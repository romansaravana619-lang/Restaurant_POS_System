import { cn } from "../../lib/cn";

const variants = {
  primary:
    "bg-[var(--sp-primary)] text-white hover:bg-[var(--sp-primary-dark)]",
  secondary:
    "border border-[var(--sp-border)] bg-[var(--sp-surface-2)] text-[var(--sp-text)] hover:bg-[var(--sp-surface-3)]",
  ghost:
    "bg-transparent text-[var(--sp-text-2)] hover:bg-[var(--sp-surface-2)] hover:text-[var(--sp-text)]",
  danger:
    "border border-[var(--sp-danger)]/40 bg-[var(--sp-danger)]/10 text-[var(--sp-danger)] hover:bg-[var(--sp-danger)]/20",
};

export function Button({
  className,
  variant = "primary",
  size = "md",
  type = "button",
  children,
  ...props
}) {
  return (
    <button
      type={type}
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-colors duration-150 disabled:cursor-not-allowed disabled:opacity-50",
        size === "sm" && "h-9 px-3 text-sm",
        size === "md" && "h-10 px-4 text-sm",
        size === "lg" && "h-11 px-5 text-sm",
        variants[variant],
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
}